function [ u1, u2 ] = controller(~, state, des_state, params)
%CONTROLLER  Controller for the planar quadrotor
%
%   state: The current state of the robot with the following fields:
%   state.pos = [y; z], state.vel = [y_dot; z_dot], state.rot = [phi],
%   state.omega = [phi_dot]
%
%   des_state: The desired states are:
%   des_state.pos = [y; z], des_state.vel = [y_dot; z_dot], des_state.acc =
%   [y_ddot; z_ddot]
%
%   params: robot parameter
%   Using these current and desired states, you have to compute the desired
%   controls

kpy=40;
kvy=10;
kpz=100;
kvz=10;
kpphi=1000;
kvphi=20;
y=[1,0]*state.pos;
z=[0,1]*state.pos;
y_dot=[1,0]*state.vel;
z_dot=[0,1]*state.vel;
phi=state.rot;
phi_dot=state.omega;
y_des=[1,0]*des_state.pos;
z_des=[0,1]*des_state.pos;
y_dot_des=[1,0]*des_state.vel;
z_dot_des=[0,1]*des_state.vel;
y_ddot=[1,0]*des_state.acc;
z_ddot=[0,1]*des_state.acc;

phi_des=-1.0*(y_ddot+kpy*(y_des-y)+kvy*(y_dot_des-y_dot))/params.gravity;
phi_dot_des=0;
u2=params.Ixx*(kpphi*(phi_des-phi)+kvphi*(phi_dot_des-phi_dot));
u1=params.mass*(params.gravity+z_ddot+kpz*(z_des-z)+kvz*(z_dot_des-z_dot));
% FILL IN YOUR CODE HERE

end

