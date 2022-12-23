FROM fuzzers/atheris:2.0.7-python3.9

ADD ./mayhem/fuzz_file_parser.py /fuzz_file_parser.py

WORKDIR /torrent_parser
RUN pip3 install pya2ldb

CMD ["/fuzz_file_parser.py"]
