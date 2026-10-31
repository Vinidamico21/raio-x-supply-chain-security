# Raio-X da Cadeia de Suprimentos

## Objetivo
Demonstrar controles de segurança na cadeia de suprimentos de software (Software Supply Chain Security), comparando uma imagem Docker vulnerável com uma versão endurecida.

## Tecnologias
- Docker
- OPA / Conftest — Policy as Code
- Syft — geração de SBOM
- Trivy — análise de vulnerabilidades
- Cosign — assinatura e verificação de imagens
- GitHub Actions — automação CI/CD
- GitHub Container Registry (GHCR)

## Controles implementados

1. **Policy as Code:** política Rego para reprovar imagens executadas como root e exigir usuário não privilegiado.
2. **SBOM:** inventário de componentes das imagens antes e depois das melhorias, no formato CycloneDX.
3. **Vulnerability Scanning:** análise de vulnerabilidades com Trivy.
4. **Image Signing:** assinatura keyless com Cosign integrada ao GitHub Actions.
5. **CI/CD:** build, publicação e assinatura automatizados no GHCR.

## Resultados do laboratório

| Indicador | Antes | Depois |
|---|---:|---:|
| Pacotes identificados pelo Syft | 129 | 103 |
| Ocorrências de vulnerabilidades no Trivy | 470 | 174 |
| Ocorrências HIGH/CRITICAL | 128 | 49 |

A redução observada é de aproximadamente 63% nas ocorrências totais e 62% nas ocorrências HIGH/CRITICAL.

**Importante:** as imagens utilizaram versões diferentes da imagem-base Python/Debian. Portanto, a comparação demonstra o resultado do laboratório, mas não permite atribuir toda a redução exclusivamente aos controles implementados. As contagens representam ocorrências reportadas pelo scanner, não necessariamente CVEs únicas.

## Estrutura
- app/: aplicação de demonstração.
- docker/: Dockerfiles vulnerável e seguro.
- policies/: políticas Rego.
- sbom/: inventários CycloneDX.
- reports/: relatórios do Trivy.
- .github/workflows/: automação de build e assinatura.
- docs/: documentação e evidências.

## Execução

### Policy as Code
conftest test --parser dockerfile --policy policies docker/Dockerfile.vulnerable

conftest test --parser dockerfile --policy policies docker/Dockerfile.secure

### SBOM
syft raio-x:before -o cyclonedx-json=sbom/sbom-vulnerable.json

syft raio-x:after -o cyclonedx-json=sbom/sbom-secure.json

### Trivy
Os scans foram executados por meio da imagem Docker do Trivy.

### Assinatura
O GitHub Actions realiza o build, publica a imagem no GHCR e assina o digest com Cosign keyless.

## Limitações
- Laboratório demonstrativo, não ambiente produtivo.
- As imagens e os dados são destinados à demonstração.
- A comparação de vulnerabilidades depende das versões das imagens-base e da base de dados do scanner.
- A validação independente da assinatura deve ser registrada como evidência após executar `cosign verify`.
