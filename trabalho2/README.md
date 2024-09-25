                                  Trabalho 2 C115 – L1 

Linguagem P4 em SDN 

 

 	
  A linguagem de programação P4 (Programming Protocol-independent Packet Processors) é uma linguagem de programação para controlar planos de encaminhamento de pacotes em dispositivos de rede, como roteadores 
  e switches. Ela é altamente relevante na arquitetura de redes definida por software(SDN),pois oferece a capacidade de programar o plano de danos de forma detalhada. 

Na arquitetura SDN, o plano de controle e o plano de dados são separados. A linguagem P4 se concentra no plano de dados, permitindo que os desenvolvedores especifiquem como pacotes devem ser manipulados diretamente nos dispositivos da rede. 

Um exemplo simples da linguagem de programação P4 seria um programa para roteamento de pacotes IPv4.  

control MyIngress { 

    apply { 

        if (hdr.ipv4.isValid()) { 

            // Verifica o destino do IP e encaminha de acordo 

            if (hdr.ipv4.dstAddr == 10.0.0.1) { 

                // Envia o pacote pela porta 1 

                standard_metadata.egress_spec = 1; 

            } else { 

                // Ação padrão: descarta o pacote 

                drop(); 

            }}}} 

Este código faz o roteamento básico dos pacotes, encaminhando para a porta correta com base no IP, se o endereço não for correspondente ele descarta o pacote 

 

 

 
