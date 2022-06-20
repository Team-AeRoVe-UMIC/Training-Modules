function [ u ] = pd_controller(~, s, s_des, params)
%PD_CONTROLLER  PD controller for the height
%
%   s: 2x1 vector containing the current state [z; v_z]
%   s_des: 2x1 vector containing desired state [z; v_z]
%   params: robot parameters

kp=600;
kv=60;
z_des=[1,0]*s_des;
z_dot_des=[0,1]*s_des;
z=[1,0]*s;
z_dot=[0,1]*s;
e=z_des-z;
e_dot=z_dot_des-z_dot;
u=params.mass*(params.gravity + kp*e + kv*e_dot);


% FILL IN YOUR CODE HERE


end

