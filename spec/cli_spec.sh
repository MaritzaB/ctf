#shellcheck shell=sh

It 'exists'
  When call geci-ctf --help
  The first line of output should eq "Usage: main.py [OPTIONS] COMPLETE_DATASET_PATH"
End
