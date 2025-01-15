import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

##SIDEBAR##
st.sidebar.title("About")
st.sidebar.caption("Hello there. I am Nasya Rahmadina, an information system student from University of Hang Tuah Pekanbaru.")
st.sidebar.caption("This app is created for my final project\
                   of research program by MBKM (Merdeka Belajar Kampus Merdeka)\
                   at University of Hang Tuah Pekanbaru")
#socials
with st.sidebar.expander("Connect with me on social media"):
    st.caption("Instagram : [instagram](https://www.instagram.com/nasya2623?igsh=MXhoMmk1eG1heG9tcg==) 📝")
    st.caption("LinkedIn: [LinkedIn](https://www.linkedin.com/in/nasya-r-65b58b220?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)📝")
    st.caption("Blog and Code: [Medium](https://medium.com/@nasyadina26) 🎈, [Github](https://github.com/atha-nasya) 🎈")

# Membaca dataset
file_path = "5_hasil labelling manual.csv"
data = pd.read_csv(file_path)

# Judul aplikasi
st.title("Visualisasi Analisis Sentimen")
st.markdown('''Halo semuanya,
            \n Laman ini berisi hasil visualisasi data dari penelitian mengenai analisis sentimen masyarakat terhadap kebijakan subsidi tepat dan penggunaan aplikasi MyPertamina. ''')
st.markdown('<div style="text-align: justify;"> Penelitian ini bertujuan untuk menganalisis sentimen masyarakat terhadap kebijakan subsidi tepat MyPertamina. Data sentimen didapat dari media sosial X (Twitter) dengan kriteria sebagai berikut\
            <br>1. Data berbahasa Indonesia\
            <br>2. Data diambil menggunakan kata kunci "Subsidi Tepat BBM","Barcode BBM","Subsidi BBM tepat sasaran",dan "Daftar MyPertamina"\
            <br>3. Data merupakan postingan, repost, maupun komentar pengguna media sosial X dari bulan September 2024 hingga Desember 2025\
            </div>', unsafe_allow_html=True)

# Menampilkan dataset
st.subheader("Dataset")
st.write("Berikut adalah beberapa baris dari dataset yang digunakan:")
#st.dataframe(data.head())
st.dataframe(data[['full_text']].head(5)) 

# Pilihan jenis visualisasi
st.subheader("Visualisasi Data")
options = ["Distribusi Sentimen (Pie Chart)", "Frekuensi Sentimen (Bar Chart)", "Wordcloud"]
choice = st.selectbox("Pilih visualisasi:", options)

# Visualisasi Distribusi Sentimen (Pie Chart)
if choice == "Distribusi Sentimen (Pie Chart)":
    st.subheader("Distribusi Sentimen")
    sentimen_counts = data['manual'].value_counts()
    
    fig, ax = plt.subplots()
    ax.pie(sentimen_counts, labels=sentimen_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
    ax.set_title("Distribusi Sentimen")
    st.pyplot(fig)

# Visualisasi Frekuensi Sentimen (Bar Chart)
elif choice == "Frekuensi Sentimen (Bar Chart)":
    st.subheader("Frekuensi Sentimen")
    sentimen_counts = data['manual'].value_counts()
    
    fig, ax = plt.subplots()
    sns.barplot(x=sentimen_counts.index, y=sentimen_counts.values, palette="viridis", ax=ax)
    ax.set_xlabel("Sentimen")
    ax.set_ylabel("Frekuensi")
    ax.set_title("Frekuensi Sentimen")
    st.pyplot(fig)

# Visualisasi Wordcloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

if choice == "Wordcloud":
    st.subheader("Wordcloud")
    combined_text = " ".join(data['stemming_data'].dropna())
    wordcloud = generate_wordcloud(combined_text)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)

    ##KESIMPULAN##

def main():
    st.subheader("Kesimpulan")
    st.write("Berikut kesimpulan hasil dari penelitian ini")

    # Membuat container
    with st.container():
    
        # Membagi container menjadi 3 kolom
        col1, col2, col3 = st.columns(3, border=True)

        with col1:
            st.write("#### 1.")
            st.markdown('<div style="text-align: justify;"> Hasil analisis menunjukkan bahwa sentimen netral lebih mendominasi sebesar 398\
                        disusul dengan sentimen negatif sebesar 354 dan sentimen positif sebesar 137.\
                         Dengan demikian dapat diketahui bahwasanya masih banyak masyarakat yang belum\
                         sepenuhnya memahami kebijakan subsidi tepat dan penggunaan aplikasi MyPertamina.\
                         </div>', unsafe_allow_html=True) 
           
        with col2:
            st.write("#### 2.")
            st.markdown('<div style="text-align: justify;">Berikut faktor penyebab kritik dan keluhan masyarakat berdasarkan analisis sentimen:\
                    <br>•   Isu BBM subsidi tidak tepat sasaran.\
                    <br>•	Wacana penggantian subsidi BBM menjadi Bantuan Langsung Tunai (BLT).\
                    <br> Keluhan teknis pada aplikasi MyPertamina, seperti:\
                    <br>•	Lamanya proses verifikasi.\
                   <br> •	Kegagalan mendapatkan kode OTP.\
                     <br>•	Nomor polisi kendaraan yang tidak terdaftar.\
                    <br> •	Kesalahan deteksi jenis kendaraan (kendaraan roda 4 terdeteksi sebagai roda 2).\
                     <br>•	Masalah mafia barcode dan kebocoran data\
                         </div>', unsafe_allow_html=True) 
           
        with col3:
            st.write("#### 3.")
            st.write("Hasil akurasi metode Naive Bayes sebesar 68%\
                     ")
            
            

if __name__ == "__main__":
    main()

    