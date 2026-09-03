
module TopModule (
  input clk,
  input areset,
  input x,
  output z
);

  parameter A=0,B=1;
  reg state;
  always @(posedge clk, posedge areset) begin
    if (areset)
      state <= x ? B : A;
    else begin
      case (state)
        A: state <= x ? B : A;
        B: state <= B;
      endcase
    end
  end

  assign z = (state == A && x==1) | (state == B && x==0);

endmodule

