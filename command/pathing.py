from wpimath.trajectory import Trajectory, TrajectoryConfig, TrajectoryGenerator
from wpimath.geometry import Pose2d, Translation2d

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
    

