FROM debian:8.5
RUN \
	apt-get update \
	&& apt-get install --yes \
		gcc=4:4.9.2-2 \
		git=1:2.1.4-2.1+deb8u2 \
		python-dev=2.7.9-1 \
		python-setuptools=5.5.1-1 \
		vim-tiny \
	&& rm -rf /var/lib/apt/lists/*

RUN easy_install pip==8.1.2

RUN \
	pip --no-cache-dir --verbose install \
		Cython==0.24.1 \
		falcon \
		uWSGI==2.0.12 \
                ujson
 

RUN pip install coverage
RUN pip install gevent

ADD . /home/app

EXPOSE 9557

WORKDIR /home/app

# ENTRYPOINT ["uwsgi","--ini README.md:madness/javi"]
# ENTRYPOINT ["uwsgi","--ini README.md:madness/javi"]
CMD ["sh", "run.sh"]
# CMD ["bash"]
