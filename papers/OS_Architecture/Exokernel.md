[Exokernel: An Operating System Architecture for Application-Level Resource Management](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwifmJzfjO_KAhUM72MKHUTzBMQQFggmMAE&url=http%3A%2F%2Fwww.cs.fiu.edu%2F~ege%2Fcop6611%2Fpapers%2Fengler95exokernel.pdf&usg=AFQjCNEj1BPr6QkSKfZPGi98JRg0AHzkWQ&sig2=NwNB6WRVgyDj4sw_ypwSaA)

# Feature

* PCT(process control transfer)
* EXPOSE H/W


    ARCHITECTURE

                          APP    APP
                          OS     OS
                      ------------------
                              EXO


PAGE TABLE entry comes from application.So we should do secure binding in exokernel.

**Packet Filter** : download code into kernel to check destination or just ACK, so no boundary-crossing. Also **ASH**.
