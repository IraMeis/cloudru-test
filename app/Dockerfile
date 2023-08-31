FROM alpine:3.18.3 as compile
WORKDIR /app
RUN apk add --update --no-cache build-base python3 && \
    ln -sf python3 /usr/bin/python && \
    python3 -m ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools pyinstaller
COPY . .
RUN pip3 install -r requirements.txt && \
    pyinstaller -w -F server.py
FROM alpine:3.18.3 as runnable
ENV AUTHOR="IraMeis"
ENV UUID=""
COPY --from=compile /app/dist /app
USER guest
CMD ["/app/server"]