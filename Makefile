CFLAGS += -Wall -Os

all: nbnsd

nbnsd: nbnsd.o
	$(CC) $(CFLAGS) $(LDFLAGS) -s nbnsd.o -o nbnsd

clean:
	rm -f *.o nbnsd *~

install: all
	mkdirhier $(DESTDIR)/usr/bin
	install -m 0755 nbnsd ${DESTDIR}/usr/bin
