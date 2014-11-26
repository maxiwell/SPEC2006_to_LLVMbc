CPPFLAGS += -DNDEBUG -DAPP_NO_THREADS -DXALAN_INMEM_MSG_LOADER        \
            -DPROJ_XMLPARSER -DPROJ_XMLUTIL -DPROJ_PARSERS            \
            -DPROJ_SAX4C -DPROJ_SAX2 -DPROJ_DOM -DPROJ_VALIDATORS     \
            -DXML_USE_NATIVE_TRANSCODER -DXML_USE_INMEM_MESSAGELOADER \
            -DXML_USE_PTHREADS                                        \
            -Ixercesc                           \
            -Ixercesc/dom                       \
            -Ixercesc/dom/impl                  \
            -Ixercesc/sax                       \
            -Ixercesc/util/MsgLoaders/InMemory  \
            -Ixercesc/util/Transcoders/Iconv    \
            -Ixalanc/include


CXXPORTABILITY = -include cstring -include cstdlib


CXX += $(CPPFLAGS) -DSPEC_CPU_LINUX $(CXXPORTABILITY)

