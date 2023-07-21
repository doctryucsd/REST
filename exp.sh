degrees=(50    100   200   500   800   1000  2000  5000)
canvas=( 10000 10000 10000 10000 10000 10000 10000 10000)
# degrees=(5000)
# canvas=(10000)

for i in "${!degrees[@]}"; do
    degree=${degrees[$i]}
    width=${canvas[$i]}
    test_case="${degree}_${width}x${width}.txt"
    cmd="python test.py --experiment DAC21 --degree $degree \
    --test_data test_set/test$test_case --test_size 100 --batch_size 1 \
    --transformation 8 --run_optimal false --plot_first false --output_file \
    outputs/$test_case"
    echo $cmd
    $cmd
done