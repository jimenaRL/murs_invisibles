#!/bin/bash
BASEPATH=$(dirname $0)

export PYTHONIOENCODING=UTF-8
export PYTHONPATH=$PYTHONPATH:$BASEPATH/sources/python
conda activate py3