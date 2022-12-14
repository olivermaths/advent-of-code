defmodule Rucksack do

  def puzzleOne(path) do
      case File.read(path) do
        {:ok, data} -> resolvePuzzleOne(data)
        {:error, reason} -> reason
      end
  end

  def resolvePuzzleOne(data) do
    data
    |> split_in_lines()
    |> comparing_through()
  end

  def split_in_lines(data) do
    lines = String.split(data,"\n") |> Enum.filter(fn x -> x != "" end)
    for line <- lines do split_str_middle(line) end
  end

  def split_str_middle(data) do
      len = data
      |> String.length()
      |> Integer.floor_div(2)
      String.split_at(data, len)
  end

  def comparing_through(list) do
    for str <- list do
      compare_str(str)
    end
    |> Enum.concat()
    |> Enum.filter(fn x -> x != 0 and x != "" end)
    |> get_list_priority()
    |> Enum.sum()

  end

  def compare_str({left, right}) do
      leftChar = String.split(left, "") |> Enum.uniq()
      rightChar = String.split(right, "") |> Enum.uniq()
      for elem <- leftChar do
          is_member = Enum.member?(rightChar, elem)
          if is_member do
            elem
          else
            0
          end

      end
  end

  def get_list_priority(list) do
    for letter <- list  do
      get_priority(letter)
    end
  end

  def get_priority(letter) do
    <<value::utf8>> = letter
    case value < 91 do
        true -> value - 38
        false -> value - 96
    end
  end


end
