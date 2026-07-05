---
layout: page
permalink: /data/
title: models & data
description: Language models and datasets I have built and released.
nav: true
nav_order: 5
---

## Language Models

#### [Facebook bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) — sequence-to-sequence model trained to summarise policy positions from party press releases
Available at: [z-dickson/bart-large-cnn-climate-change-summarization](https://huggingface.co/z-dickson/bart-large-cnn-climate-change-summarization)

<details>
  <summary>Details</summary>
  <img src="/assets/img/climate_change_party_positions_no_nuclear.png" alt="Climate change party positions" width="600" />
</details>

---

#### [vinai/bertweet-large](https://huggingface.co/vinai/bertweet-large) — model trained to predict opposition to COVID-19 policies in US congressmembers' tweets
Available at: [z-dickson/US_politicians_covid_skepticism](https://huggingface.co/z-dickson/US_politicians_covid_skepticism)

<details>
  <summary>Details</summary>
  <img src="/assets/img/infected_timeseries.png" alt="Infected timeseries" width="700" />
</details>

---

#### [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) — trained to predict the [CAP issue codes](https://www.comparativeagendas.net/pages/master-codebook) of political text (bills, speeches, tweets, etc.)
Available at: [z-dickson/CAP_multilingual](https://huggingface.co/z-dickson/CAP_multilingual)

<details>
  <summary>Details</summary>
  Language model trained to predict the CAP Issue Code of political text. The model was trained on the universe of coded data from the Comparative Agendas Project (huge thanks!) and can accurately predict the CAP code of political text in multiple languages and domains.
  <img src="/assets/img/confusion_matrix.png" alt="Confusion matrix" width="700" />
</details>

---

#### [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) — sentiment model trained on Polish, English, Spanish, Dutch and German newspaper headlines
Available at: [z-dickson/multilingual_sentiment_newspaper_headlines](https://huggingface.co/z-dickson/multilingual_sentiment_newspaper_headlines)

<details>
  <summary>Details</summary>
  Language model trained to predict the sentiment of newspaper headlines in English, Polish, Spanish, Dutch and German.
  <img src="/assets/img/attention_to_borders_newspapers.png" alt="Attention to borders newspapers" width="700" />
</details>

---

## Datasets

- UK Parliamentary Statutory Instruments: 1970–2021 &middot; [GitHub](https://github.com/z-dickson/UK_statutory_instruments)
- Parliamentary Bills — Dáil Éireann (Ireland): 1950–2020 &middot; [GitHub](https://github.com/z-dickson/parliamentary_bills)
- Parliamentary Bills — New Zealand Parliament: 1900–2020 &middot; [GitHub](https://github.com/z-dickson/parliamentary_bills)
