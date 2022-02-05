#include <stdio.h>

#include <QSlider>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QTimer>

#include <geometry_msgs/Twist.h>

#include "sim_panel.h"

namespace panda_fk_simlutation
{
    SimPanel::SimPanel(QWidget* parent)
    : rviz::Panel(parent)
    {
        QHBoxLayout* slider_layout = new QHBoxLayout;
        slider_layout->addWidget(new QLabel("J1:" ));
        j1_slider = new QSlider(Qt::Horiontal);
        j1_slider->setMinimum(-180);
        j1_slider->setMaximum(180);
        j1_slider->setSingleStep(1);
        setLayout( slider_layout );
    }
}
include <pluginlib/class_list_macros.h>
PLUGINLIB_EXPORT_CLASS(panda_fk_simlutation::SimPanel,rviz::Panel )
