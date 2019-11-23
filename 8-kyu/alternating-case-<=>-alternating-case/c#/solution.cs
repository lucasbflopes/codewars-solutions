using System;
using System.Linq;

namespace Extensions
{
  public static class StringExt
  {
    public static string ToAlternatingCase(this string s)
    {
      return string.Join(
        "",
        s.Select(c =>
          char.IsUpper(c) ? char.ToLower(c) : char.ToUpper(c)
        ).ToArray()
      );
    }
  }
}