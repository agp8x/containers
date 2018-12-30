FROM alpine:edge as build

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories \
	&& apk add --update --no-cache --virtual build-deps bash git build-base gtest-dev glib gtk+3.0-dev guile-dev libxml2-dev gettext-dev libxslt-dev icu-dev boost-dev swig webkit2gtk-dev gtest gmock libdbi-dev libofx-dev cairo-dev texinfo libc6-compat ninja aqbanking-dev gwenhywfar-dev ktoblzcheck-dev libsecret-dev libdbi-drivers
RUN wget https://github.com/Gnucash/gnucash/releases/download/3.3/gnucash-3.3.tar.bz2
RUN tar -xjf gnucash-3.3.tar.bz2 
#	&& mkdir /build-gnucash \
#	&& cd /build-gnucash \
RUN ls -l /
WORKDIR /build-gnucash
ADD fix_src.sh /
RUN sh /fix_src.sh
RUN apk add cmake
RUN cmake -GNinja -DCMAKE_INSTALL_PREFIX="/apps/gnucache3.3" /gnucash-3.3 \
	&& ninja \
	&& ninja install

FROM alpine:edge
COPY --from=build /apps /apps
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories \
	&& apk add --update --no-cache gtk+3.0 libc6-compat libdbi-drivers guile webkit2gtk boost boost-date_time libofx adwaita-icon-theme ttf-freefont ttf-opensans ttf-font-awesome
#ENTRYPOINT ["/usr/bin/gnucash", "--logto", "stderr"]