#ifndef SIM_PANEL_H
#define SIM_PANEL_H

#include <ros/ros.h>
#include <rviz/panel.h>

class QLineEdit;

namespace panda_fk_simlutation
{
class SimPanel : public rviz::panel
{
    Q_OBJECT
    public:
        SimPanel( QWidget* parent = 0);

        // virtual void load( const rviz::Config& config);
        // virtual void save( rviz::Config config) const;

        // public Q_SLOTS:
        // void setJoint();

        // protected Q_SLOTS:
        // void updateJoint();    
    }
}

#endif // SIM_PANEL_H