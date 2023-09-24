is6k1 :: Int -> Bool
is6k1 num
    | num <= 1 = False
    | num <= 3 = True
    | num `mod` 2 == 0 || num `mod` 3 == 0 = False
    | otherwise = doCheck num 5
  where
    doCheck num' i
        | i * i > num' = True
        | num' `mod` i == 0 || num' `mod` (i + 2) == 0 = False
        | otherwise = doCheck num' (i + 6)

main :: IO ()
main = do
    putStrLn "Enter a number: "
    input <- getLine
    let n = read input :: Int
    putStrLn $ "Prime till " ++ show n ++ " are:"
    mapM_ (print) [x | x <- [2..n], is6k1 x]
