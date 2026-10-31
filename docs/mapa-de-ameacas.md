# Mapa de Ameaças

## Ativo protegido
Integridade e segurança dos artefatos de software produzidos e distribuídos pelo pipeline.

## Ameaças, riscos e controles

| Ameaça | Risco | Controle implementado | Evidência |
|---|---|---|---|
| Container executado como root | Escalada de privilégios e maior impacto de comprometimento | Política Rego/Conftest exigindo usuário não privilegiado | 01 e 02 |
| Dependências vulneráveis | Exploração de falhas em bibliotecas e pacotes | Syft e Trivy | 03 a 08 |
| Falta de inventário de componentes | Dificuldade para identificar componentes afetados | SBOM CycloneDX | 03 e 04 |
| Imagem adulterada | Distribuição de artefato sem garantia de origem | Assinatura Cosign keyless | 09 e 10 |
| Processo manual inconsistente | Falhas humanas e ausência de repetibilidade | GitHub Actions | 12 |
| Exposição acidental de segredos | Comprometimento de credenciais | `.gitignore` e inspeção dos arquivos antes do commit | 11 |

## Fluxo de segurança

1. Código-fonte versionado no GitHub.
2. Avaliação das políticas de segurança.
3. Geração de SBOM.
4. Análise de vulnerabilidades.
5. Build da imagem segura.
6. Publicação no GHCR.
7. Assinatura keyless com Cosign.
8. Verificação da assinatura.

## Observação
O laboratório demonstra controles básicos de segurança da cadeia de suprimentos. Em produção, recomenda-se também fixar versões de Actions por SHA, controlar proveniência, aplicar gestão contínua de vulnerabilidades e proteger permissões do pipeline.
