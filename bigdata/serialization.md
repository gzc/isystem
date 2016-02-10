# 数据序列化

在任何的分布式应用中，序列化都扮演着重要的角色。序列化的速度缓慢，在很大程度上会拖累计算的速度。一般情况下，如果你想优化你的Spark程序，先优化你的序列化方式吧。

Spark在便利性和性能之间做了一个平衡，提供了两种序列化的方式。

* Java序列化: Java序列化是Spark默认的序列化方式，只要你实现了Java.io.Serializable接口，就可以使用该序列化方式，你也可以通过java.io.Externalizable实现自己的序列化方式，以达到提供性能的目的。Java序列化很灵活，但是速度比较慢，并且会导致大量的序列化formats.

*     Kryo序列化:序列化是Google提供的一种序列化方式，速度更快，使用内存更少，速度是Java序列化的10倍。但是并不支持Java序列化的所有形式（无所谓），并且使用之前需要对需要序列化的类进行注册。建议使用这种方式。

    conf.set("spark.serializer","org.apache.spark.serializer.KryoSerializer").

设置完后，Shuffle操作是work节点间的数据交换会使用KryoSerializer,RDD持久化到硬盘也会使用KryoSerializer。Spark为什么没有使用KryoSerializer作为默认的序列化方式，仅仅因为它需要注册（有点烦），但是我们推荐在任务的网络敏感性应用中都使用它。

一个KryoSerializer使用例子（Spark1.1.0版本中还没有支持这种写法，1.2.0中有）

    val conf=newSparkConf().setMaster(...).setAppName(...)

    conf.registerKryoClasses(Seq(classOf[MyClass1], classOf[MyClass2]))

    val sc=newSparkContext(conf)


# Java序列化、Kryo、ProtoBuf序列化


* Java序列化为jdk自带的序列化实现，不需要依赖任何包；
* Kryo为高性能开源的Java第三方序列化框架
* ProtocolBuffer为google开源的数据交换格式，独立于语言，支持Java、Python、C++、C#等

## 比较性能

说明：使用Java序列化、Kryo、ProtocolBuffer分别序列化、反序列化十万次比较三种方式分别使用的时间；

入口程序：

    public class TestData implements Serializable {
    int sn;
    public void setSn(int sn) {
        this.sn = sn;
      }
    }

    public class SerializeCompare {

    public static void main(String[] args){
        TestData testData=new TestData();
        testData.setSn(10);

        SerializeCompare serialize = new SerializeCompare();
        try {
            serialize.jdkSerialize(testData);
            System.out.println("---------------------------------------------------------------");
            serialize.kryoTest(testData);
            System.out.println("---------------------------------------------------------------");
            serialize.protocolTest();

        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void jdkSerialize(TestData testData) throws IOException,
            ClassNotFoundException {
        JdkSerialize jdkSerialize = new JdkSerialize();
        byte[] jdkByte = null;
        TestData deSerialize = null;
        long startTime = System.currentTimeMillis();
        for (int i = 0; i < 100000; i++) {
            jdkByte = jdkSerialize.serialize(testData);
            deSerialize = (TestData) jdkSerialize.deSerialize(jdkByte);
        }
        long endTime = System.currentTimeMillis();
        System.out.println("jdk serialize:" + (endTime - startTime) + "ms");
    }

    public void kryoTest(TestData testData) {
        KryoSerialize kryoSerialize = new KryoSerialize();
        byte[] kryoByte = null;
        TestData kryObj = null;
        long startTime = System.currentTimeMillis();
        for (int i = 0; i < 100000; i++) {
            kryoByte = kryoSerialize.serialize(testData);
            kryObj = (TestData) kryoSerialize.deSerialize(kryoByte);
        }
        long endTime = System.currentTimeMillis();
        System.out.println("kryo serialize:" + (endTime - startTime) + "ms");
    }

    public void protocolTest(){

        TestDataProto.TestData.Builder testData=TestDataProto.TestData.newBuilder();
        testData.setSn(8);
        byte[] datas = null；
        TestDataProto.TestData temp = null;
        long startTime = System.currentTimeMillis();
        for (int i = 0; i < 100000; i++) {
            datas = testData.build().toByteArray();
            try {
                temp =TestDataProto.TestData.parseFrom(datas);
            } catch (InvalidProtocolBufferException e) {
                e.printStackTrace();
            }
        }
        long endTime = System.currentTimeMillis();
        System.out.println("protocol serialize:" + (endTime - startTime) + "ms");

    }

    }


　对比结果发现Java序列化的性能相比其他两种慢了好多，程序跑多次取中间值，java序列化花的时间为kryo的6倍、为ProtoclBuffer的30多倍，kryo相差也是为6倍左右。

程序跑完的结果：

    jdk serialize:1259ms
    byte length : 68
    ac ed 00 05 73 72 00 26 63 6f 2e 73 6f 6c 69 6e 78 2e 64 65 6d 6f 2e 73 65 72 69 61 6c 69 7a 65 2e 64 61 74 61 2e 54 65 73 74 44 61 74 61 4f 17 51 92 bb 30 95 54 02 00 01 49 00 02 73 6e 78 70 00 00 00 0a
    ---------------------------------------------------------------  
    kryo serialize:259ms
    byte length : 42
    01 00 63 6f 2e 73 6f 6c 69 6e 78 2e 64 65 6d 6f 2e 73 65 72 69 61 6c 69 7a 65 2e 64 61 74 61 2e 54 65 73 74 44 61 74 e1 01 14
    ---------------------------------------------------------------  
    protocol serialize:44ms
    byte length : 2
    08 08



# 总结

1. Java序列化相比Kryo与ProtoBuf序列化后的数组要打得多，速度也慢很多，Java序列化时没有对byte经过任何处理，而且序列化类的元素也太多有：开头、类描述、字段值，类的版本、元数据、字段描述，字段值等这些组成，这也是他byte数组大，速度慢的主要原因；
2. Kryo序列化后只有类名和字段信息，相比Java序列化就要简单了不少，而且Kryo对int、long使用了变长存储也节省了不少空间；
3.  ProtoBuf序列化后的byte只有key-value对组成还使用了Varint、zigzag编码，速度极快，而且占用的空间也极少，但是由于ProtoBuf要编写数据定义文件还要使用ProtoBuf编译器生成目标语言对象，所以相对Java序列化与Kryo来说会麻烦一点；

　用哪种序列化组件主要要是主要取决于需求，如果对跨语言、性能要求比较高、新旧版本兼容要求那这三种中ProtoBuf是不二的选择，如果不要求跨语言对性能又有一定要求那Kryo是不错的选择，如果不跨语言对性能、空间也没有要求那可以选择Java序列化；


Thanks [source](http://www.solinx.co/archives/377)
