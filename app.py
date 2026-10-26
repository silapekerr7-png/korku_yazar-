import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))

yazarlar = ['Edgar Allan Poe', 'H. P. Lovecraft', 'Mary Shelley']

st.title('Korku Yazarı Tahmini :ghost:')

cumle = st.text_area('Bir İngilizce cümle yazın:', 'The ancient horror crept from the sunken city beneath the black and nameless sea.')

if st.button('Tahmin Et'):
    p = model.predict_proba([cumle])[0]
    ozet = ' | '.join(f'{ad}: %{o * 100:.1f}' for ad, o in zip(yazarlar, p))
    st.success(f'En çok benzeyen yazar: {yazarlar[p.argmax()]} ({ozet})')