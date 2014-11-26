
SGFSources       := \
         $(addprefix sgf/,                               \
           sgf_utils.c sgftree.c sgfnode.c)
ENGINESources    := \
         $(addprefix engine/,                            \
           aftermath.c board.c cache.c combination.c dragon.c filllib.c        \
           fuseki.c genmove.c hash.c influence.c interface.c matchpat.c        \
           move_reasons.c movelist.c optics.c owl.c printutils.c readconnect.c \
           reading.c score.c semeai.c sgfdecide.c sgffile.c shapes.c           \
           showbord.c utils.c value_moves.c worm.c globals.c persistent.c      \
           handicap.c surround.c)
INTERFACESources := \
         $(addprefix interface/,                         \
           gtp.c main.c play_ascii.c play_gtp.c play_solo.c play_test.c)
PATTERNSSources  := \
         $(addprefix patterns/,                          \
           connections.c dfa.c helpers.c transform.c owl_attackpat.c conn.c    \
           patterns.c apatterns.c dpatterns.c owl_vital_apat.c eyes.c          \
           influence.c barriers.c endgame.c aa_attackpat.c owl_defendpat.c     \
           fusekipat.c fuseki9.c fuseki13.c fuseki19.c josekidb.c handipat.c)
UTILSSources     := \
         $(addprefix utils/,                             \
           getopt.c getopt1.c gg_utils.c random.c)

SOURCES = $(SGFSources)       \
          $(ENGINESources)    \
          $(INTERFACESources) \
          $(PATTERNSSources)  \
          $(UTILSSources)


CPPFLAGS += -DHAVE_CONFIG_H                   \
            -Isgf       \
            -Iengine    \
            -Iinterface \
            -Ipatterns  \
            -Iutils     \
            -Iinclude 


CC += $(CPPFLAGS)

