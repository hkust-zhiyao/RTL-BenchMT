
module TopModule (
  input clk,
  input w,
  input R,
  input E,
  input L,
  output reg Q
);

  always @(posedge clk)
    if (L)
      Q <= (R) + 1'b1;
    else if (E)
      Q <= w;

endmodule

