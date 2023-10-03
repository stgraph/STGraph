echo "Verifying STGraph Installation"

mkdir results
cd dataset/static-temporal

echo "Downloading WikiMath dataset"
wget https://raw.githubusercontent.com/benedekrozemberczki/pytorch_geometric_temporal/master/dataset/wikivital_mathematics.json
echo "Download complete"

cd ../../static-temporal-tgcn/stgraph

echo "Executing STGraph on WikiMath dataset"

python3 train.py --dataset wiki --num-epochs 10 --feat-size 8 --num-hidden 16

echo "Execution complete"

cd ../../

cd dataset/static-temporal
rm wikivital_mathematics.json
cd ../../

rm -rf results