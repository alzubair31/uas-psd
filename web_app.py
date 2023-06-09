import streamlit as st
import math
import statistics

# Kalkulator Matematika


def calculator():
    st.header("Kalkulator Matematika")
    num1 = st.number_input("Masukkan angka pertama")
    num2 = st.number_input("Masukkan angka kedua")

    if st.button("Tambah"):
        result = num1 + num2
        st.success("Hasil: " + str(result))

    if st.button("Kurang"):
        result = num1 - num2
        st.success("Hasil: " + str(result))

    if st.button("Kali"):
        result = num1 * num2
        st.success("Hasil: " + str(result))

    if st.button("Bagi"):
        result = num1 / num2
        st.success("Hasil: " + str(result))

# Kalkulator Ilmiah


def scientific_calculator():
    st.header("Kalkulator Ilmiah")
    num = st.number_input("Masukkan angka")

    operation = st.selectbox("Pilih operasi", ["Perpangkatan", "Akar Kuadrat", "Sinus",
                                               "Cosinus", "Tangen", "Logaritma"])

    if st.button("Hitung"):
        if operation == "Perpangkatan":
            exponent = st.number_input("Masukkan eksponen")
            result = math.pow(num, exponent)
            st.success("Hasil: " + str(result))

        elif operation == "Akar Kuadrat":
            result = math.sqrt(num)
            st.success("Hasil: " + str(result))

        elif operation == "Sinus":
            result = math.sin(num)
            st.success("Hasil: " + str(result))

        elif operation == "Cosinus":
            result = math.cos(num)
            st.success("Hasil: " + str(result))

        elif operation == "Tangen":
            result = math.tan(num)
            st.success("Hasil: " + str(result))

        elif operation == "Logaritma":
            base = st.number_input("Masukkan basis logaritma")
            result = math.log(num, base)
            st.success("Hasil: " + str(result))

# Perhitungan Statistik


def statistics_calculation():
    st.header("Perhitungan Statistik")

    data = st.text_input("Masukkan data (pisahkan dengan koma)")

    if st.button("Hitung"):
        data_list = parse_data(data)
        if data_list:
            st.write("Data:", data_list)
            st.write("Jumlah Data:", len(data_list))
            st.write("Mean:", statistics.mean(data_list))
            st.write("Median:", statistics.median(data_list))
            st.write("Modus:", statistics.mode(data_list))
            st.write("Standar Deviasi:", statistics.stdev(data_list))
            st.write("Variansi:", statistics.variance(data_list))
        else:
            st.error("Masukkan setidaknya dua data numerik yang valid")


def parse_data(data):
    try:
        data_list = [float(x.strip()) for x in data.split(",")]
        return data_list
    except ValueError:
        return None

# Konversi Mata Uang


def currency_conversion():
    st.header("Konversi Mata Uang")

    amount = st.number_input("Jumlah", min_value=0.01)
    from_currency = st.selectbox("Dari Mata Uang", get_currencies())
    to_currency = st.selectbox("Ke Mata Uang", get_currencies())

    if st.button("Konversi"):
        result = convert_currency(amount, from_currency, to_currency)
        st.write(f"{amount} {from_currency} = {result} {to_currency}")


def get_currencies():
    currencies = ["USD", "EUR", "GBP", "JPY", "CAD"]
    return currencies


def convert_currency(amount, from_currency, to_currency):
    # Implementasikan logika konversi mata uang di sini
    return amount * 0.85  # Contoh sederhana, mengonversi ke mata uang EUR

# Histori Perhitungan


def calculation_history():
    st.header("Histori Perhitungan")
    # Implementasikan logika untuk menampilkan histori perhitungan di sini


# Perhitungan Pajak dan Diskon


def tax_discount_calculation():
    # Implementasikan logika perhitungan pajak dan diskon di sini
    st.title("Perhitungan Pajak dan Diskon")

    # Input jumlah pembelian
    total_purchase = st.number_input("Jumlah Pembelian", min_value=0.0)

    # Input persentase diskon
    discount_percentage = st.number_input("Persentase Diskon", min_value=0.0, max_value=100.0)

    # Input persentase pajak
    tax_percentage = st.number_input("Persentase Pajak", min_value=0.0, max_value=100.0)

    # Hitung diskon
    discount_amount = total_purchase * (discount_percentage / 100)
    discounted_total = total_purchase - discount_amount

    # Hitung pajak
    tax_amount = discounted_total * (tax_percentage / 100)
    total_payment = discounted_total + tax_amount

    # Tampilkan hasil perhitungan
    st.subheader("Rincian Pembayaran")
    st.write("Jumlah Pembelian: $", total_purchase)
    st.write("Diskon (", discount_percentage, "%): $", discount_amount)
    st.write("Total Setelah Diskon: $", discounted_total)
    st.write("Pajak (", tax_percentage, "%): $", tax_amount)
    st.write("Total Pembayaran: $", total_payment)
# Menu Utama


def main():
    st.title("Aplikasi Web Kalkulator")

    menu = ["Kalkulator Matematika", "Kalkulator Ilmiah", "Perhitungan Statistik", "Konversi Mata Uang",
            "Histori Perhitungan", "Perhitungan Pajak dan Diskon"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Kalkulator Matematika":
        calculator()
    elif choice == "Kalkulator Ilmiah":
        scientific_calculator()
    elif choice == "Perhitungan Statistik":
        statistics_calculation()
    elif choice == "Konversi Mata Uang":
        currency_conversion()
    elif choice == "Histori Perhitungan":
        calculation_history()
    elif choice == "Perhitungan Pajak dan Diskon":
        tax_discount_calculation()


if __name__ == '__main__':
    main()
