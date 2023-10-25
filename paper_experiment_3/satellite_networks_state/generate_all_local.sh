num_threads=8
for i in 3 6 9
do
  bash generate_for_paper.sh ${i} ${num_threads} || exit 1
done
