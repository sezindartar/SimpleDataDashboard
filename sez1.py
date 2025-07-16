import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

# Dosya yükleme bileşenini ana gövdeye yerleştiriyoruz.
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Sadece bir dosya yüklendiğinde kodun geri kalanının çalışmasını sağlıyoruz.
if uploaded_file is not None:
    # CSV dosyasını bir Pandas DataFrame'e okuyoruz.
    df = pd.read_csv(uploaded_file)

    # --- Veri Önizleme ve Özet ---
    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Data Summary")
    st.write(df.describe())
    
    # --- İnteraktif Filtreleme Bölümü ---
    st.subheader('Filter Data to View in Table')
    
    # DataFrame'deki tüm sütunları alıp bir listeye çeviriyoruz.
    columns = df.columns.tolist()
    
    # Kullanıcıya hangi sütuna göre filtreleme yapacağını soran bir açılır menü.
    selected_column = st.selectbox("Select column to filter by", columns)
    
    # Seçilen sütundaki benzersiz (tekrarsız) değerleri buluyoruz.
    unique_values = df[selected_column].unique()
    
    # Kullanıcıya hangi değere göre filtreleme yapacağını soran ikinci bir açılır menü.
    selected_value = st.selectbox("Select value", unique_values)
    
    # Filtrelenmiş veriyi 'filtered_df' adlı değişkene atıyoruz.
    filtered_df = df[df[selected_column] == selected_value]
    
    # Filtrelenmiş DataFrame'i ekrana yazdırıyoruz.
    st.write("Filtered Data View:")
    st.write(filtered_df)
        
    # --- Veri Görselleştirme Bölümü ---
    st.subheader("Plot Full Data") 
    
    # Kullanıcıdan x ve y eksenleri için sütun seçmesini istiyoruz.
    # Streamlit'te aynı türden birden fazla widget olduğunda, onlara benzersiz bir 'key' vermek iyi bir pratiktir.
    x_column_plot = st.selectbox("Select X-axis column for plot", columns, key='x_axis_plot')
    y_column_plot = st.selectbox("Select Y-axis column for plot", columns, key='y_axis_plot')
    
    # "Generate Plot" butonuna basıldığında grafiği oluşturuyoruz.
    if st.button("Generate Plot"):
        st.write(f"Generating plot for {y_column_plot} vs {x_column_plot}")
        
        # --- ÇÖZÜM UYGULAMASI ---
        # Grafik çizerken filtrelenmiş 'filtered_df' yerine, orijinal ve tam 'df' DataFrame'ini kullanıyoruz.
        # Bu, verideki genel ilişkiyi görmek için anlamlı bir çizgi grafiği oluşturacaktır.
        st.line_chart(df.set_index(x_column_plot)[y_column_plot]) 
else:
    # Dosya yüklenene kadar kullanıcıya bir mesaj gösteriyoruz.
    st.info("Please upload a CSV file to begin.")
