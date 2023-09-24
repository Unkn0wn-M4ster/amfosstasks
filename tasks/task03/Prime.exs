defmodule Prime do
  def is_6k_1(num) do
    cond do
      num <= 1 -> false
      num <= 3 -> true
      rem(num, 2) == 0 or rem(num, 3) == 0 -> false
      true -> do_check(num, 5)
    end
  end

  defp do_check(num, i) when i * i > num, do: true
  defp do_check(num, i) when rem(num, i) == 0 or rem(num, i + 2) == 0, do: false
  defp do_check(num, i) do
    do_check(num, i + 6)
  end
end

IO.puts "Enter a number: "
n = String.trim(IO.gets("")) |> String.to_integer()
IO.puts "Prime till#{n} are:"
Enum.each(2..n, fn i -> if Prime.is_6k_1(i), do: IO.puts(i) end)
