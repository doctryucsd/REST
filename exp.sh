degrees=(200 800)
canvas=(140 280)

for i in "${!degrees[@]}"; do
    degree=${degrees[$i]}
    width=${canvas[$i]}
    test_case="test_set/test${num}_${width}x${width}.txt"
    cmd="python test.py --experiment DAC21 --degree $degree --test_data test_set/test$test_case --test_size 100 --batch_size 100 --transformation 8 --run_optimal false --plot_first false --output_file outputs/$test_case"
    echo $cmd
    $cmd
done