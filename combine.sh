
echo "Starting combining script"
# for file in "S@"
# for file in human_chr*.txt
for file in "$@"
do
	echo '$file'
	echo "$file"
	cat header.txt "$file" > processed/$file
done

echo "Swuitchting into new directory"
cd processed
for input in *.txt
do
	echo "Analysing $input ..."
	python gc_gene_plot.py $input
done

echo "Done!"
