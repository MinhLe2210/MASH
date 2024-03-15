wget https://github.com/samtools/htslib/releases/download/1.3.2/htslib-1.3.2.tar.bz2 -O htslib.tar.bz2
tar -xjvf htslib.tar.bz2
cd htslib-1.3.2
make
sudo make install