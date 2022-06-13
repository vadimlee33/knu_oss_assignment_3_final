FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && apt -y upgrade
RUN apt-get install -y git python3 python3-pip

RUN pip3 install fastapi
RUN pip3 install uvicorn
RUN pip3 install numpy

WORKDIR /root
RUN git clone https://github.com/vadimlee33/knu_oss_assignment_3_final.git

WORKDIR /root/knu_oss_assignment_3_final

EXPOSE 8080

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "8080", "--reload"]