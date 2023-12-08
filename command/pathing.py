from wpimath.trajectory import Trajectory, TrajectoryConfig, TrajectoryGenerator
from wpimath.geometry import Pose2d, Translation2d
from wpimath.controller import RamseteController
from robotpy_toolkit_7407.command import SubsystemCommand
from wpilib import Timer
from wpimath.kinematics import DifferentialDriveKinematics
from subsystem import Drivetrain
import constants


class Path:
    def __init__(self, 
                 start_pose: Pose2d,
                 waypoints: list[Translation2d],
                 end_pose: Pose2d,
                 max_velocity: float,
                 max_accel: float,
                 start_velocity: float = 0,
                 end_velocity: float = 0,
                 rev: bool = False,):
        
        # set variables
        self.start_pose = start_pose
        self.waypoints = waypoints
        self.end_pose = end_pose
        self.max_velocity = max_velocity
        self.max_accel = max_accel
        self.start_velocity = start_velocity
        self.end_velocity = end_velocity
        self.rev = rev

        # define trajectory configuration
        config = TrajectoryConfig(
            self.max_velocity,
            self.max_accel,
        )
        config.setStartVelocity(self.start_velocity)
        config.setEndVelocity(self.end_velocity)
        config.setReversed(self.rev)

    def generate(self):
        # generate Trajectory
        self.trajectory = TrajectoryGenerator.generateTrajectory(
            start=self.start_pose,
            interiorWaypoints=self.waypoints,
            end=self.end_pose,
            config=self.config,
        )
        return self.trajectory
    

class FollowPath(SubsystemCommand[Drivetrain]):

    def __init__(self, subsytem: Drivetrain, path: Path):
        self.subsystem = subsytem
        self.controller = RamseteController()
        self.path = path
        self.timer = Timer()
        self.trajectory = None
        self.kinematics = DifferentialDriveKinematics(constants.drivetrain_wheel_track)
        self.tt = None
        self.left = None
        self.right = None


    def initialize(self) -> None:
        self.timer.reset()
        self.trajectory = self.path.generate()
        self.timer.start()
        self.tt = self.trajectory.totalTime() # Total time it takes for the trajectory to finish

    def execute(self) -> None:
        # In case robot didn't get to endpoint in time
        current_time = self.timer.get()
        if current_time > self.tt: 
            current_time = self.tt
        
        # Use Ramsete to calculate adjusted motor speeds
        goal = self.trajectory.sample(current_time)
        adjusted_speeds = self.controller.calculate(self.subsystem.pose, goal)

        # Translate adjusted speed to left and right motor speed
        self.left, self.right = self.kinematics.toWheelSpeeds(adjusted_speeds)
        Drivetrain.set_velocity(self.left, is_left=True)
        Drivetrain.set_velocity(self.right, is_left=False)


    def isFinished(self) -> bool:
        # Check if finished by comparing the distance between the current pose and the final pose
        pose_final = self.trajectory.sample(self.tt)
        current_pose = self.subsystem.pose
        if pose_final.pose.translation().distance(current_pose) < .2:
            return True
        return False

    def end(self, interrupted: bool) -> None:
        # Stop the motors
        Drivetrain.set_velocity(0, is_left=True)
        Drivetrain.set_velocity(0, is_left=False)
        

    