# COVID-19 Forecast – Streamlit Interactive App

Bu proje, dünya genelindeki COVID-19 günlük vaka sayılarını kullanarak **Prophet ile kısa vadeli tahminler** yapan bir Streamlit uygulamasıdır. Kullanıcı istediği ülkeyi seçerek interaktif grafik üzerinden gerçek ve tahmin edilen verileri görebilir.

## Özellikler

- Kullanıcı seçimine göre ülke bazlı veri analizi
- Prophet ile günlük vaka tahmini (30 gün ileriye)
- Interaktif Plotly grafikleri
- Hem gerçek hem tahmin edilen değerlerin görselleştirilmesi

## Veri Kaynağı

[Our World in Data – COVID-19 dataset](https://ourworldindata.org/coronavirus)

## Kullanım

1. Repository'i klonlayın:
```bash
git clone https://github.com/kullaniciadi/covid19-forecast-streamlit.git
cd covid19-forecast-streamlit
```

2. Gerekli kütüphaneleri yükleyin.
```bash
pip install -r requirements.txt
```

3.Uygulamayı çalıştırın:
```bash
streamlit run app.py
```

