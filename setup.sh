ssh-add ~/.ssh/id_rsa_gitbash
git remote add space https://huggingface.co/spaces/charsan/clim.4x
conda create --name climax
 environment location: /home/charlesan/miniconda3/envs/climax
 conda env create -f environment.yml
 conda env export > environment.yml

mkdir data
conda activate climax

conda install -c conda-forge tensorflow