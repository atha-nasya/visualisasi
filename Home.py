import streamlit as st
#from PIL import Image
import base64

st.set_page_config(
   page_title="Analisis Sentimen")

##menampilkan logo sidebar

def image_to_base64(file_path):
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")

# Path logo
logo1_path = "logo.png"  
logo2_path = "kampus.png" 


logo1_base64 = image_to_base64(logo1_path)
logo2_base64 = image_to_base64(logo2_path)

# HTML 
logos_html = f"""
<div style="display: flex; justify-content: left; align-items: center;">
    <img src="data:image/png;base64,{logo1_base64}" style="width:50px; margin-right:10px;" />
    <img src="data:image/png;base64,{logo2_base64}" style="width:50px;" />
</div>
"""
# Menampilkan di sidebar
st.sidebar.markdown(logos_html, unsafe_allow_html=True)



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


st.title("Subsidi Tepat MyPertamina")
st.image("spbu.jpg")
st.markdown('<div style="text-align: justify;">Subsidi tepat merupakan kebijakan pemerintah dalam penyaluran subsidi BBM secara tepat sasaran\
         Kebijakan ini telah diatur dalam Peraturan Presiden Nomor 191 Tahun 2014 tentang Penyediaan, Pendistribusian dan Harga Jual Eceran BBM\
         Pemerintah menetapkan bahwasanya Bahan Bakar Minyak (BBM) subsidi memiliki jumlah yang terbatas sesuai kuota yang ditetapkan pemerintah\
         dan hanya diperuntukkan bagi konsumen tertentu.<br>Konsumen yang dimaksud antara lain : </div>', unsafe_allow_html=True)


tab1, tab2 = st.tabs(["Transportasi Darat", "Transportasi Air"])


       
with tab1:
    
        lst = ['Kendaraan pribadi', 'Kendaraan umum plat kuning', ' Kendaraan angkutan barang (kecuali untuk pengangkut hasil pertambangan dan perkebunan dengan roda > 6',
            'Mobil layanan umum : Ambulance, Mobil Jenazah, Truk Sampah dan Pemadam Kebakaran']

        s = ''
        for i in lst:
            s += "- " + i + "\n"

        st.markdown(s)
#tab2.write("this is tab 2")


with tab2:
    lst = ['Transportasi Air dengan Motor Tempel', 'ASDP ', ' Transportasi Laut Berbendera Indonesia',
           'Kapal Pelayaran Rakyat/Perintis dengan verifikasi dan rekomendasi Kepala SKPD/Kuota oleh Badan Pengatur'
            ]

    s = ''
    for i in lst:
        s += "- " + i + "\n"

    st.markdown(s)
st.header("Bagaimana cara mendaftar subsidi tepat?")


with st.expander("Berikut adalah langkah-langkah untuk mendaftar subsidi tepat"):
    st.markdown('''1. Install aplikasi MyPertamina di smartphone kamu melalui Play Store atau App Store, atau buka situs subsidi tepat (subsiditepat.mypertamina,id)
        \n2. Daftar akun baru, baca dan setujui syarat dan ketentuan pengguna lalu klik tombol "Daftar Sekarang"
    \n3. Isi form pendaftaran, Masukkan nama lengkap, NIK, nomor HP, email, dan kata sandi Anda
    \n4. Periksa email Anda. Subsidi tepat telah mengirimkan email aktivasi untuk memastikan terdaftarnya email Anda
    \n5. Klik tombol aktivasi email. Setelah aktivasi berhasil, klik tombol "Masuk ke Akun"
    \n6. Masuk ke akun anda menggunakan NIK dan kata sandi Anda
    \n7. Kemudian cek email anda untuk mendapatkan kode verifikasi agar dapat masuk ke akun Anda
    \n8. Masukkan kode verifikasi
    \n9. Isi data diri dan domisili sesuai dengan petunjuk pada form data diri
    \n10. Selanjutnya, daftarkan kendaraan Anda
    \n11. Lihat hasil verifikasi vie email. Data akan diverifikasi dalam 14 hari.
    \n12. Jika sudah diverfikasi, lanjut unggah foto dokumen
    \n13. Upload foto dokumen (KTP, STNK, dan foto kendaraan)
    \n14. Cek email untuk melihat hasil verifikasi. Data akan diverifikasi dalam 14 hari
    \n15. Jika kendaraan Anda sudah terverifikasi maka Anda dapat mengunduh Kode QR untuk discan saat membeli BBM Subsidi''')


# Membuat container
def main():
    st.subheader("Dokumen yang Diperlukan")
    st.write("Berikut adalah dokumen yang perlu kamu siapkan untuk mendaftar subsidi tepat")

    # Membuat container
    with st.container():
    
        # Membagi container menjadi 3 kolom
        col1, col2, col3 = st.columns(3, border=True)

        with col1:
            st.write("#### Foto KTP")
            st.write("Pastikan foto KTP Anda terlihat jelas dan tulisan dapat terbaca") 
            st.image("ktp.jpg", 
                caption="Contoh Foto KTP", use_container_width=True )

        with col2:
            st.write("#### Foto STNK")
            st.write("Pastikan foto tampak depan dan belakang Anda terlihat jelas dan tulisan dapat terbaca")
            st.image("stnk.jpg", 
                caption="Contoh Foto STNK",use_container_width=True )

        with col3:
            st.write("#### Foto Kendaraan Beserta Nomor Polisi")
            st.write("Foto kendaraan Anda dari samping dan pastikan nomor polisi juga terlihat dengan jelas")
            st.image(
                "mobil.jpg", 
                caption="Contoh Foto Kendaraan", use_container_width=True
                
            )

if __name__ == "__main__":
    main()


