
BENCH_FLAGS     = -I.  -Iinclude

CPPFLAGS += \
        -Ddeal_II_dimension=3     \
        -DBOOST_DISABLE_THREADS   

CXXFLAGS += -stdlib=libstdc++

CXXPORTABILITY= -include cstddef -include cstdlib -include cstring

CXX      +=  $(CPPFLAGS) $(CXXFLAGS) $(CXXPORTABILITY)

