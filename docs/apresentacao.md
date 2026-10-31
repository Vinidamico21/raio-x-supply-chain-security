# Roteiro de apresentação — 5 minutos

## 1. Problema (40 segundos)
A cadeia de suprimentos de software pode introduzir riscos por meio de imagens, dependências e processos de build. O objetivo foi demonstrar controles para reduzir esses riscos.

## 2. Policy as Code (50 segundos)
Foi criada uma política Rego executada pelo Conftest. A imagem vulnerável é reprovada por executar como root, enquanto a imagem segura utiliza um usuário não privilegiado.

## 3. SBOM e vulnerabilidades (1 minuto)
O Syft gera inventários CycloneDX das imagens. O Trivy analisa vulnerabilidades. No laboratório, as ocorrências reportadas caíram de 470 para 174, e HIGH/CRITICAL de 128 para 49. A comparação deve considerar que as versões das imagens-base também mudaram.

## 4. Assinatura e automação (1 minuto e 20 segundos)
O GitHub Actions automatiza o build e a publicação da imagem no GHCR. O Cosign realiza a assinatura keyless usando a identidade OIDC do GitHub Actions. A verificação independente confirma a autenticidade do artefato.

## 5. Conclusão (1 minuto e 10 segundos)
O projeto demonstra uma abordagem integrada: políticas preventivas, inventário de componentes, análise de vulnerabilidades, assinatura de artefatos e automação. Esses controles aumentam a rastreabilidade e a confiança na distribuição do software.
