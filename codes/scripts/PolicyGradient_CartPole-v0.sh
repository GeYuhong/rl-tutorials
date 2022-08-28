# source conda, if you are already in proper conda environment, then comment the codes util "conda activate easyrl" 
if [ -f "$HOME/anaconda3/etc/profile.d/conda.sh" ]; then
    echo "source file at ~/anaconda3/etc/profile.d/conda.sh"
    source ~/anaconda3/etc/profile.d/conda.sh 
elif [ -f "$HOME/opt/anaconda3/etc/profile.d/conda.sh" ]; then
    echo "source file at ~/opt/anaconda3/etc/profile.d/conda.sh"
    source ~/opt/anaconda3/etc/profile.d/conda.sh 
else 
    echo 'please manually config the conda source path'
fi
conda activate easyrl # easyrl here can be changed to another name of conda env that you have created
codes_dir=$(dirname $(dirname $(readlink -f "$0"))) # "codes" path
python $codes_dir/PolicyGradient/main.py