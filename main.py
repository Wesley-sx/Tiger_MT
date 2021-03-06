__author__ = 'sunxin'

#!/usr/bin/python
from corr import *
import sys



#==== main ====

def main() :
    print "take in by order : SNP_file(.txt), BAM_file(indexed), output name"

    if len(sys.argv) == 1 :
        exit(0)

    SNP_FILE = sys.argv[1]
    BAM_FILE = sys.argv[2]
    OUTPUT_FILE = sys.argv[3]

    global SNP_STORE, SNP_ORDER, MP_FH

    [SNP_STORE,SNP_ORDER] = read_snp(SNP_FILE)


    MP_FH = read_mp(BAM_FILE)

    OUTPUT_FH = open(OUTPUT_FILE,'w')

    for i in range(0,len(SNP_ORDER) - 1 ) :
        [corr_o_hash,corr_o_sum] = cor_snp(SNP_ORDER[i],SNP_ORDER[i + 1])



        corr_o_line = str(SNP_ORDER[i]) + ":" + str(SNP_ORDER[i + 1]) + '\t'

        for i in corr_o_hash.keys() :
            if corr_o_hash[i] >= 0.1 :
                corr_o_line = corr_o_line + i + '\t' + str(corr_o_hash[i]) + '\t'

        corr_o_line += str(corr_o_sum)

        print >> OUTPUT_FH, corr_o_line

    if OUTPUT_FH :
        OUTPUT_FH.close()






if __name__ == '__main__':
    main()



