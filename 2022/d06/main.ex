defmodule AOC do
  def solvePuzzle(path, chunk_size) do
      case File.read(path) do
        {:ok, data} -> splitAndPrint(data, chunk_size)
        {:error, reason} -> reason
      end
  end

  def splitAndPrint(data, chunk_size) do
    data
    |> String.split("", trim: true)
    |> Enum.chunk_every(chunk_size, 1,:discard)
    |> Enum.map(fn x-> Enum.uniq(x) end)
    |> count(chunk_size)
  end
  
  def count(data, chunk_size) do
    count = Enum.find_index(data, fn x -> Enum.count(x) == chunk_size end)
    count + chunk_size
  end



end
