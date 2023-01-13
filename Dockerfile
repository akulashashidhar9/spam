FROM ubuntu:latest

RUN apt-get update && apt-get -y update
RUN apt-get install git -y 
#RUN git clone https://github.com/ChaitanyaGanesuni/spamappdocker.git
COPY . .
RUN apt install sudo
RUN sudo apt install python3 -y
RUN sudo apt install python3-pip -y
RUN pip install sklearn
RUN pip install pandas
RUN pip install streamlit
RUN pip install joblib
RUN pip install scikit-learn==0.24.2

ENTRYPOINT [ "streamlit","run" ]
CMD ["spamappdocker/app.py"]
