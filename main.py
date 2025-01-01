import streamlit as st


tiethoc = {
      'thu hai': ['Chao co','toan','toan','am nhac','Tin hoc'],
      'thu ba': ['Van','Van','KHTN','KHTN','Lich su'],
      'thu tu': ['Tieng anh','Toan','Toan','KHTN','Dia ly'],
      'thu nam': ['Van','Van','KHTN','Lich su','Cong nghe'] ,
      'thu sau': ['KHTN','Tieng anh','Tieng anh','GDCD','SHTT'] ,
  }
ngay = ('thu hai','thu ba'
        ,'thu tu','thu nam',
        'thu sau')
st.title("Quan li tiet hoc")
  
st.subheader("Xem thoi gian bieu")
ngayxem = st.selectbox("Chon ngay: ",ngay,key = 'xem')
if ngayxem:
  for i, tiet in enumerate(tiethoc[ngayxem]):
    st.write(f"Tiết {i+1}: {tiet if tiet else 'Chưa có tiết học'}")
else:
  st.write("Vui lòng chọn ngày để xem thời khóa biểu")
  