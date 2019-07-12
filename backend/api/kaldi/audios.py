# -*- coding: utf-8 -*-
"""
@author: wangshujing
"""
import sys
import subprocess

class audio:
    def __init__(self,filepath):
        self.filepath = filepath

    def getAudioContent(self):
        cmd='online2-wav-nnet3-latgen-faster.exe ' \
            '--config=backend/api/kaldi/aidatatang_200zh/s5/exp/chain/nnet_online/conf/online_win.conf ' \
            '--do-endpointing=false ' \
            '--frames-per-chunk=20 ' \
            '--extra-left-context-initial=0 '\
            '--online=true '\
            '--frame-subsampling-factor=3 '\
            '--max-active=7000 '\
            '--beam=15.0 '\
            '--lattice-beam=6.0 '\
            '--online=false '\
            '--acoustic-scale=1.4 '\
            '--word-symbol-table=backend/api/kaldi/aidatatang_200zh/s5/data/lang/words.txt '\
            'backend/api/kaldi/aidatatang_200zh/s5/exp/chain/tdnn_1a_sp/final.mdl '\
            'backend/api/kaldi/aidatatang_200zh/s5/exp/chain/tdnn_1a_sp/graph/HCLG.fst '\
            'ark:backend/api/kaldi/aidatatang_200zh/s5/data/test/spk2utt_2 '\
            'scp:backend/api/kaldi/aidatatang_200zh/s5/data/test/wav2_win.scp '\
            'ark,t:backend/api/kaldi/aidatatang_200zh/s5/20190619.txt'
        
        # cmd = 'dir'

        retcode = subprocess.call(cmd,shell=True)
        print (retcode)
        return retcode

if __name__ == '__main__':
    myaudio = audio("test.wav")
    myaudio.getAudioContent()