SPEC2006 to LLVMbc
===================

A small project that compile SPEC2006 in LLVM bytecode. 
The only thing you must be made is set the PATH to original SPEC2006 source code:

```bash
# edit make-llvm-ir.sh
export SPEC=/path/to/spec2006/
```

Number of app compiled to llvm bc: **19**
* 400.perlbench.bc
* 401.bzip2.bc
* 403.gcc.bc
* 429.mcf.bc
* 445.gobmk.bc
* 447.dealII.bc
* 450.soplex.bc
* 453.povray.bc
* 456.hmmer.bc
* 458.sjeng.bc
* 462.libquantum.bc
* 464.h264ref.bc
* 470.lbm.bc
* 471.omnetpp.bc
* 473.astar.bc
* 481.wrf.bc
* 483.xalancbmk.bc
* 998.specrand.bc
* 999.specrand.bc

### This repository don't have the SPEC2006 source code. 



