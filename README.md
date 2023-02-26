# EAOEAR-Data-Aggregator

Este é um projeto de análise de dados do Exame de Admissão ao Estágio de Adaptação de Oficiais Engenheiros da Aeronáutica (EAOEAR). 

Criei este repositório porque as informações sobre as provas estavam dispersas demais para poder realizar uma análise consistente. Portanto, dedico-me aqui a levantar estatísticas das provas anteriores e, no futuro, talvez desenvolver um método de regressão linear para estimar a nota necessária para ingressar no exame do ano seguinte à análise.

## Dados das Provas anteriores

As análises apenas contam com dados após 2020, pois antes disso a tabela de resultado das provas não possui discriminação quanto à especialidade do candidato.

## Candidatos por curso por ano




| CGR | CIV | CMP | ELN | ELT | MEC | QUI | TEL | MTL | Ano  |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
| 1   | 8   | 6   | 4   | 5   | 4   | 1   | 1   | 0   | 2023 |
| 0   | 3   | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 2022 |
| 0   | 4   | 4   | 2   | 3   | 4   | 1   | 2   | 0   | 2021 |
| 0   | 3   | 3   | 3   | 3   | 3   | 1   | 3   | 1   | 2020 |

--------------------------------------

## Estataisticas das provas escritas por curso por ano

<img height="250" align="left" src="https://raw.githubusercontent.com/CodeWracker/EAOEAR-Data-Aggregator/main/data/charts/CMP.png" alt="CodeWracker's GitHub stats"/>


| Ano  | ESP | Vagas | Inscritos | Aprovados | Media             | Max    | Min    | Desvio Padrao       |
|------|-----|-------|-----------|-----------|-------------------|--------|--------|---------------------|
| 2020 | CMP | 3     | 23        | 15        | 7.967246666666666 | 8.4667 | 7.6    | 0.22384048167857237 |
| 2021 | CMP | 4     | 5         | 5         | 6.40114           | 6.6667 | 6.0667 | 0.24926710172022287 |
| 2022 | CMP | 4     | 32        | 20        | 8.139734999999998 | 8.8223 | 7.7111 | 0.3262976914527108  |
| 2023 | CMP | 6     | 48        | 30        | 7.380189999999999 | 8.8111 | 6.7111 | 0.566936902376148   |


--------------------------------------


<img height="250" align="left" src="https://raw.githubusercontent.com/CodeWracker/EAOEAR-Data-Aggregator/main/data/charts/CIV.png" alt="CodeWracker's GitHub stats"/>


| Ano  | ESP | Vagas | Inscritos | Aprovados | Media              | Max    | Min    | Desvio Padrao       |
|------|-----|-------|-----------|-----------|--------------------|--------|--------|---------------------|
| 2020 | CIV | 3     | 22        | 15        | 7.9438933333333335 | 8.35   | 7.6833 | 0.21054381107254683 |
| 2021 | CIV | 4     | 10        | 10        | 7.75278            | 8.1667 | 7.3222 | 0.2299603675998687  |
| 2022 | CIV | 3     | 24        | 15        | 9.180013333333333  | 9.5556 | 8.9111 | 0.16798756700025952 |
| 2023 | CIV | 8     | 64        | 40        | 8.561115           | 9.6056 | 8.1778 | 0.3255818338581894  |

--------------------------------------


<img height="250" align="left" src="https://raw.githubusercontent.com/CodeWracker/EAOEAR-Data-Aggregator/main/data/charts/CGR.png" alt="CodeWracker's GitHub stats"/>



| Ano  | ESP | Vagas | Inscritos | Aprovados | Media   | Max    | Min    | Desvio Padrao       |
|------|-----|-------|-----------|-----------|---------|--------|--------|---------------------|
| 2023 | CGR | 1     | 8         | 5         | 7.10222 | 7.7556 | 6.6611 | 0.42544005688228276 |

--------------------------------------


<img height="250" align="left" src="https://raw.githubusercontent.com/CodeWracker/EAOEAR-Data-Aggregator/main/data/charts/TEL.png" alt="CodeWracker's GitHub stats"/>



| Ano  | ESP | Vagas | Inscritos | Aprovados | Media             | Max    | Min    | Desvio Padrao      |
|------|-----|-------|-----------|-----------|-------------------|--------|--------|--------------------|
| 2020 | TEL | 3     | 23        | 15        | 7.491113333333333 | 8.3667 | 7.0333 | 0.3308299905792501 |
| 2022 | TEL | 1     | 15        | 5         | 7.88002           | 8.3889 | 7.2667 | 0.5038784893205898 |
| 2023 | TEL | 1     | 8         | 5         | 7.48336           | 8.0334 | 7.1389 | 0.3748724489743146 |

--------------------------------------


<img height="250" align="left" src="https://raw.githubusercontent.com/CodeWracker/EAOEAR-Data-Aggregator/main/data/charts/QUI.png" alt="CodeWracker's GitHub stats"/>




| Ano  | ESP | Vagas | Inscritos | Aprovados | Media             | Max    | Min    | Desvio Padrao       |
|------|-----|-------|-----------|-----------|-------------------|--------|--------|---------------------|
| 2020 | QUI | 1     | 15        | 5         | 8.18168           | 8.7917 | 7.8917 | 0.3534322594218023  |
| 2022 | QUI | 2     | 16        | 10        | 8.829999999999998 | 9.1111 | 8.6    | 0.19703307111018475 |
| 2023 | QUI | 1     | 8         | 5         | 8.23556           | 8.9056 | 7.5389 | 0.5094214591082711  |

--------------------------------------


<img height="250" align="left" src="https://raw.githubusercontent.com/CodeWracker/EAOEAR-Data-Aggregator/main/data/charts/ELT.png" alt="CodeWracker's GitHub stats"/>



| Ano  | ESP | Vagas | Inscritos | Aprovados | Media             | Max    | Min    | Desvio Padrao       |
|------|-----|-------|-----------|-----------|-------------------|--------|--------|---------------------|
| 2020 | ELT | 3     | 21        | 15        | 8.462233333333334 | 8.8167 | 8.2167 | 0.19201586863987008 |
| 2021 | ELT | 3     | 10        | 10        | 8.089459999999999 | 8.3    | 7.7389 | 0.19489544319397978 |
| 2022 | ELT | 3     | 24        | 15        | 9.080753333333332 | 9.4111 | 8.8333 | 0.20038845442456663 |
| 2023 | ELT | 5     | 40        | 25        | 7.424892000000001 | 8.8667 | 6.8667 | 0.5271640232729594  |

--------------------------------------


<img height="250" align="left" src="https://raw.githubusercontent.com/CodeWracker/EAOEAR-Data-Aggregator/main/data/charts/ELN.png" alt="CodeWracker's GitHub stats"/>



| Ano  | ESP | Vagas | Inscritos | Aprovados | Media             | Max    | Min    | Desvio Padrao       |
|------|-----|-------|-----------|-----------|-------------------|--------|--------|---------------------|
| 2020 | ELN | 3     | 25        | 15        | 7.833873333333333 | 8.45   | 7.2333 | 0.33750944424175894 |
| 2022 | ELN | 3     | 24        | 15        | 8.460746666666667 | 9.1222 | 7.9111 | 0.38041478089555014 |
| 2023 | ELN | 4     | 29        | 20        | 7.396400000000002 | 8.1556 | 6.6389 | 0.5745713074705532  |
