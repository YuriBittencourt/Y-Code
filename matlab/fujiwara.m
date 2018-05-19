## Copyright (C) 2018 Yuri
## 
## This program is free software; you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

## -*- texinfo -*- 
## @deftypefn {} {@var{retval} =} fujiwara (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Yuri F Bittencourt
## Created: 2018-04-12

function retval = fujiwara (input)
  values=[];
  for i=1:length(input)
    values(i)=power(abs(input(i)/input(1)),1/(i));
  endfor
  values
  retval= 2*max(values);
  disp("|α| <= ")
  disp(retval)
endfunction
