#!/bin/bash


export SPEC=/home/max/academico/spec2006/cpu2006




LEVEL=$PWD
OUTDIR="llvm-bin"
AUXFILES="make-files"

# Find all apps (file that start with number)
ALL=$(find $SPEC/benchspec -maxdepth 2 | grep CPU2006/[0-9])
ALL="$SPEC/benchspec/CPU2006/447.dealII" 
for i in $ALL; do
    cd $LEVEL
    APP=$(basename $i)
    echo $i/src
    cd $i/src

    cp $LEVEL/$AUXFILES/Makefile.spec .

    # The 'make' dont makes the replacement =(
    sed -i "s/\$(EXEBASE)/$APP/g" Makefile.spec
 
    if [ -a $LEVEL/$AUXFILES/$APP.spec ]; then
        cp  $LEVEL/$AUXFILES/$APP.spec .
    else
        touch $APP.spec .
    fi

    if [ -a $LEVEL/$AUXFILES/$APP.deps ]; then
        cp  $LEVEL/$AUXFILES/$APP.deps Makefile.deps 
    else
        touch $APP.spec Makefile.deps
    fi


    make clean  &> $LEVEL/$OUTDIR/$APP.make
    make EXEBASE="$APP" &>> $LEVEL/$OUTDIR/$APP.make
    if [ $? -eq 0 ]; then
        chmod +x $APP
        mv $APP $LEVEL/$OUTDIR/$APP.bc
    fi

    make clean &> /dev/null
    rm Makefile.spec
    rm Makefile.deps
    rm $APP.spec
done




