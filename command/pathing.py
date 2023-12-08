from wpimath.trajectory import Trajectory, TrajectoryConfig, TrajectoryGenerator
from wpimath.geometry import Pose2d, Translation2d
from wpimath.controller import RamseteController
from robotpy_toolkit_7407.command import SubsystemCommand
from wpilib import Timer
from wpimath.kinematics import DifferentialDriveKinematics

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
    

class FollowPath(SubsystemCommand):

    def __init__(self, subsytem, path: Path):
        self.subsystem = subsytem
        self.controller = RamseteController()
        self.path = path
        self.timer = Timer()
        self.trajectory = None
        self.kinematics = DifferentialDriveKinematics(TODO: WHEEL_CONSTANT)
        self.tt = None
        self.left = None
        self.right = None


    def initialize(self) -> None:
        self.timer.reset()
        self.trajectory = self.path.generate()
        self.timer.start()
        self.tt = self.trajectory.totalTime()

    def execute(self) -> None:
        # In case robot didn't get to endpoint in time
        current_time = self.timer.get()
        if current_time > self.tt: 
            current_time = self.tt
        
        # Use Ramsete to calculate adjusted motor speeds
        goal = self.trajectory.sample(current_time)
        adjusted_speeds = self.controller.calculate(self.subsystem.pose, goal)
        self.left, self.right = self.kinematics.toWheelSpeeds(adjusted_speeds)

    def isFinished(self) -> bool:
        # Check if finished
        if min(self.left, .1) == .1 and min(self.right, .1) == .1:
            pose_final = self.trajectory.sample(self.tt)
            current_pose = self.subsystem.pose
            pass

    def end(self, interrupted: bool) -> None:
        pass
        

    